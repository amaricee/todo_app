<template>
  <li class="todo-item">
    <input
      type="checkbox"
      :checked="Number(todo.is_completed) === 1"
      @change="$emit('toggle', todo)"
    />

    <span
      v-if="!isEdit"
      :class="{ completed: Number(todo.is_completed) === 1 }"
      :data-priority="todo.priority"
    >
      {{ todo.title }} | P{{ todo.priority }} | {{ todo.due_date }}
    </span>

    <!-- MODE EDIT -->
    <div v-else class="edit-form">
      <input v-model="editTitle" />
      <select v-model="editPriority">
        <option :value="1">Low</option>
        <option :value="2">Medium</option>
        <option :value="3">High</option>
      </select>
      <input type="date" v-model="editDueDate" />
    </div>

    <button v-if="!isEdit" @click="startEdit">Edit</button>
    <button v-if="isEdit" @click="saveEdit">Simpan</button>
    <button @click="$emit('delete', todo.id)">Hapus</button>
  </li>
</template>

<script>
export default {
  props: {
    todo: Object,
  },

  data() {
    return {
      isEdit: false,
      editTitle: "",
      editPriority: 1,
      editDueDate: "",
    };
  },

  methods: {
    startEdit() {
      this.isEdit = true;
      this.editTitle = this.todo.title;
      this.editPriority = this.todo.priority;
      this.editDueDate = this.todo.due_date;
    },

    saveEdit() {
      this.$emit("edit", {
        id: this.todo.id,
        title: this.editTitle,
        priority: this.editPriority,
        due_date: this.editDueDate,
      });
      this.isEdit = false;
    },
  },
};
</script>
