import Client from './api'

export const RegisterUser = async (username, password) => {
  const res = await Client.post('/users/register', {
    username,
    password
  })
  return res.data
}

export const LoginUser = async (username, password) => {
  const res = await Client.post('/users/login', {
    username,
    password
  })
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
