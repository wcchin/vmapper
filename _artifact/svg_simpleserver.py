
import bottle
import cairo
import cStringIO
import base64
import datetime
import time

bottle.debug(True)

def time_page(a_page):
    def _time_page(*args, **kwargs):
        start   = time.time()
        retval  = a_page(*args, **kwargs)
        end     = time.time()
        if bottle.DEBUG is True: print "%s, %0.2fms" % (repr(a_page), (end - start) * 1000)
        return retval
    return _time_page

def cache_page(a_page_cache, timeout):
    def _cache_page(a_page):
        def __cache_page(*args, **kwargs):
            page_id = repr(a_page)
            if page_id not in a_page_cache or a_page_cache[page_id][0] <= time.time():
                    if bottle.DEBUG is True: print "cache miss or refresh (%s)" % (page_id,)
                    retval                  = a_page(*args, **kwargs)
                    a_page_cache[page_id]   = (time.time() + timeout, retval)
                    return retval
            else:
                if bottle.DEBUG is True: print "cache hit (%s)" % (page_id,)
                return a_page_cache[page_id][1]
        return __cache_page
    return _cache_page

a_page_cache = dict()

def svg_stream(width, height):
    def _svg_stream(a_page):
        def __svg_stream(*args, **kwargs):
            an_svg_file = cStringIO.StringIO()
            a_surface   = cairo.SVGSurface(an_svg_file, width, height)
            a_context   = cairo.Context(a_surface)
            a_page(a_context, *args, **kwargs)
            a_surface.finish()
            bottle.response.content_type = 'image/svg+xml'
            return "data:image/svg+xml;base64,%s" % (base64.b64encode(an_svg_file.getvalue()),)
        return __svg_stream
    return _svg_stream
    
@bottle.route('/window.svg')
@time_page
@cache_page(a_page_cache, 0.5)
@svg_stream(640, 480)
def window(a_context):
    a_context.set_source_rgba(0.99607, 1.0, 0.76, 1.0)
    a_context.select_font_face("sans")
    a_context.set_font_size(32)
    a_context.move_to(140, 170)
    a_context.show_text("window.svg")

@bottle.route('/clock.svg')
@time_page
@cache_page(a_page_cache, 0.5)
@svg_stream(640, 480)
def clock(a_context):
    the_time = datetime.datetime.now()
    
    a_context.set_line_width(6.0)

    #   (degrees / second) * (pi / 180) ~= (360 / 60) * (3.14159 / 180) ~= 0.1047196
    a_context.set_source_rgba(0.57, 0.48, 0.34, 1.0)
    a_context.arc(240, 180, 30, (the_time.second + 1) * 0.1047196, (the_time.second - 1) * 0.1047196)
    a_context.stroke()

    a_context.set_source_rgba(0.71, 0.73, 0.42, 1.0)
    a_context.arc(240, 180, 30, (the_time.second - 0.3)* 0.1047196, (the_time.second + 0.3) * 0.1047196)
    a_context.stroke()

    a_context.set_line_width(10.0)

    a_context.set_source_rgba(0.49, 0.16, 0.21, 1.0)
    a_context.arc(240, 180, 43, (the_time.minute + 1.7) * 0.1047196, (the_time.minute - 1.7) * 0.1047196)
    a_context.stroke()

    a_context.set_source_rgba(0.8, 0.57, 0.35, 1.0)
    a_context.arc(240, 180, 43, (the_time.minute - 0.6)* 0.1047196, (the_time.minute + 0.6) * 0.1047196)
    a_context.stroke()

    a_context.set_line_width(11.0)

    a_context.set_source_rgba(0.71, 0.73, 0.42, 1.0)
    a_context.arc(240, 180, 60, (the_time.hour + 1.7) * 0.1047196, (the_time.hour - 1.7) * 0.1047196)
    a_context.stroke()

    a_context.set_source_rgba(0.99607, 1.0, 0.76, 1.0)
    a_context.arc(240, 180, 60, (the_time.hour - 0.6)* 0.1047196, (the_time.hour + 0.6) * 0.1047196)
    a_context.stroke()
    
    a_context.select_font_face("sans")
    a_context.set_font_size(32)
    a_context.move_to(320, 340)
    a_context.show_text("%02d:%02d:%02d" % (the_time.hour, the_time.minute, the_time.second))

@bottle.route('/:a_file')
@time_page
def static_file(a_file):
    return bottle.static_file(a_file, root='./')

bottle.run(host='127.0.0.1', port=8080)