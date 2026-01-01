<template>
  <form @submit.prevent="submit">
    <input v-model="title" placeholder="Judul todo" />

    <select v-model="priority">
      <option :value="1">Low</option>
      <option :value="2">Medium</option>
      <option :value="3">High</option>
    </select>

    <input type="date" v-model="due_date" />

    <button type="submit">Tambah</button>
  </form>
</template>

<script>
export default {
  emits: ['add'],

  data() {
    return {
      title: '',
      priority: 1,
      due_date: ''
    }
  },

  methods: {
    submit() {
      if (!this.title || !this.due_date) {
        alert('Judul & deadline wajib diisi')
        return
      }

      this.$emit('add', {
        title: this.title,
        priority: this.priority,
        due_date: this.due_date
      })

      this.title = ''
      this.priority = 1
      this.due_date = ''
    }
  }
}
</script>
