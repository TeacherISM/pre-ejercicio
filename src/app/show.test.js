import app from '../app'
import request from 'supertest'

describe('show', () => {
  test('Api responds with 200', async () => {
    const response = await request(app).get('/api/hello')
    expect(response.statusCode).toBe(200)
  })
})