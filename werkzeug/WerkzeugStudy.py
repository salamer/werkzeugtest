from werkzeug.wrappers import Response

def application(environ,start_response):
    response=Response('hello world!',mimetypr='text/plain')
    return response(environ,start_response)
    
    
#             expended version
#def application(environ,start_response):
#    request=Request(environ)
#    text='hello %s!' % request.args.get('name','world')
#    response=Response(text,mimetype='text/plain')
#    return response(environ,start_response)
