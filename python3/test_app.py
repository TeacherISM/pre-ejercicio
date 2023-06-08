import app

def test_handler():
    event = {}
    context = {}
    response = app.handler(event, context)

    assert response['statusCode'] == 200
    assert response['body'] == 'Hola, Soy Karla Mondragón!!'