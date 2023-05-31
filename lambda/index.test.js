const { handler } = require('./index');

describe('handler', () => {
  it('should return a response with status code 200 and body "Hola Sebastian!"', async () => {
    const event = {}; // Add your event payload here if needed
    const expectedResponse = {
      statusCode: 200,
      body: JSON.stringify('Hola Sebastian!'),
    };

    const response = await handler(event);

    expect(response).toEqual(expectedResponse);
  });
});
