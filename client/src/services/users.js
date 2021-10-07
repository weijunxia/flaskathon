import Client from './api'

export const CreateUser = async username => {
  const res = await Client.post('/users', { username })
  return res.data
}

export const FindUserById = async id => {
  const res = await Client.get(`/users/${id}`)
  return res.data
}

export const RemoveUser = async id => {
  const res = await Client.delete(`/users/${id}`)
  return res.data
}
