import axios from 'axios'

const API = 'http://127.0.0.1:5000/api'

export default {
  getTodos() {
    return axios.get(`${API}/todos`)
  },

  addTodo(data) {
    return axios.post(`${API}/todos`, data)
  },

  updateTodo(id, data) {
    return axios.patch(`${API}/todos/${id}`, data)
  },

  updateStatus(id, is_completed) {
    return axios.patch(`${API}/todos/${id}/status`, {
      is_completed
    })
  },

  deleteTodo(id) {
    return axios.delete(`${API}/todos/${id}`)
  }
}
