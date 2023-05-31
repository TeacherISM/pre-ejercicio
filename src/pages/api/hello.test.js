import handler from './handler';

describe('handler', () => {
  let req;
  let res;

  beforeEach(() => {
    req = {
      method: '',
    };
    res = {
      status: jest.fn(),
      json: jest.fn(),
    };
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  test('should respond with "Hello, world!" and status 200 for GET request', () => {
    req.method = 'GET';

    handler(req, res);

    expect(res.status).toHaveBeenCalledWith(200);
    expect(res.json).toHaveBeenCalledWith({ message: 'Hello, world!' });
  });

  test('should respond with "Method Not Allowed" and status 405 for non-GET request', () => {
    req.method = 'POST';

    handler(req, res);

    expect(res.status).toHaveBeenCalledWith(405);
    expect(res.json).toHaveBeenCalledWith({ message: 'Method Not Allowed' });
  });
});
