import Client from './api'

export const GetPosts = async () => {
  try {
    const res = await Client.get('/posts')
    return res.data
  } catch (error) {
    throw error
  }
}

export const CreatPost = async data => {
  try {
    const res = await Client.post('/posts', data)
    return res.data
  } catch (error) {
    throw error
  }
}
