import Client from './api'

export const CreateUser = async username => {
  try {
    const res = await Client.post('/users', { username })
    return res.data
  } catch (error) {
    throw error
  }
}

export const FindUserById = async id => {
  try {
    const res = await Client.get(`/users/${id}`)
    return res.data
  } catch (error) {
    throw error
  }
}

export const RemoveUser = async id => {
  try {
    const res = await Client.delete(`/users/${id}`)
    return res.data
  } catch (error) {
    throw error
  }
}
