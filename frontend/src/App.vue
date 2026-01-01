<template>
  <h1>Todo App</h1>

  <TodoForm @add="addTodo" />

  <TodoList
    :todos="todos"
    @toggle="toggleStatus"
    @delete="deleteTodo"
    @edit="editTodo"
  />
</template>

<script>
import TodoForm from "./components/TodoForm.vue";
import TodoList from "./components/TodoList.vue";
import todoApi from "./services/todoApi";

export default {
  components: { TodoForm, TodoList },

  data() {
    return {
      todos: [],
    };
  },

  methods: {
    async fetchTodos() {
      const res = await todoApi.getTodos();
      this.todos = res.data;
    },

    async addTodo(data) {
      await todoApi.addTodo(data);
      this.fetchTodos();
    },

    async toggleStatus(todo) {
      await todoApi.updateStatus(todo.id, todo.is_completed === 1 ? 0 : 1);
      this.fetchTodos();
    },

    async editTodo(data) {
      await todoApi.updateTodo(data.id, data);
      this.fetchTodos();
    },
    async deleteTodo(id) {
      await todoApi.deleteTodo(id);
      this.fetchTodos();
    },
  },

  mounted() {
    this.fetchTodos();
  },
};
</script>
