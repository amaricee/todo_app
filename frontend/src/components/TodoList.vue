<template>
  <ul>
    <TodoItem
      v-for="todo in todos"
      :key="todo.id"
      :todo="todo"
      @toggle="$emit('toggle', $event)"
      @delete="$emit('delete', $event)"
      @edit="$emit('edit', $event)"
    />
  </ul>
</template>

<script>
import TodoItem from './TodoItem.vue'

export default {
  components: { TodoItem },

  props: {
    todos: Array
  }
}
</script>
