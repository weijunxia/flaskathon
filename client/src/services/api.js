import axios from 'axios'

export const BASE_URL =
  process.env.NODE_ENV === 'production' ? 'google.com' : 'http://localhost:8080'

const Client = axios.create({ baseURL: BASE_URL })

export default Client
