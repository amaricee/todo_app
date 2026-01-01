<template>
  <div>
    <table class="todo-table">
      <thead>
        <tr>
          <th>Status</th>
          <th>Daftar Tugas</th>
          <th>Prioritas</th>
          <th>Deadline</th>
          <th>Keterangan</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="todo in todos"
          :key="todo.id"
          :class="{ completed: Number(todo.is_completed) === 1 }"
        >
          <td>
            <input
              type="checkbox"
              :checked="Number(todo.is_completed) === 1"
              @change="$emit('toggle', todo)"
            />
          </td>
          <td>{{ todo.title }}</td>
          <td>
            <span :class="'priority p' + todo.priority">
              {{ ["Low", "Medium", "High"][todo.priority - 1] }}
            </span>
          </td>
          <td>{{ todo.due_date }}</td>
          <td class="status-text">
            {{ Number(todo.is_completed) === 1 ? "Selesai" : "Belum Selesai" }}
          </td>
          <td class="actions">
            <button class="edit-btn" @click="openEditModal(todo)">Edit</button>
            <button class="delete-btn" @click="openDeleteModal(todo)">
              Hapus
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal Edit -->
    <div class="modal modal-edit" v-if="showModal">
      <div class="modal-content">
        <h3>Edit Todo</h3>
        <input v-model="editTitle" placeholder="Judul todo" />
        <select v-model="editPriority">
          <option :value="1">Low</option>
          <option :value="2">Medium</option>
          <option :value="3">High</option>
        </select>
        <input type="date" v-model="editDueDate" />

        <div class="modal-buttons">
          <!-- Tombol Simpan (hijau) -->
          <button class="save-btn" @click="saveEdit">Simpan</button>
          <!-- Tombol Batal (merah) -->
          <button class="cancel-btn" @click="closeModal">Batal</button>
        </div>
      </div>
    </div>

    <!-- Modal Konfirmasi Hapus -->
    <div class="modal modal-delete" v-if="showDeleteModal">
      <div class="modal-content">
        <h3>Konfirmasi Hapus</h3>
        <p>
          Apakah Anda yakin ingin menghapus "<strong>{{
            deletingTodo?.title
          }}</strong
          >"?
        </p>
        <div class="modal-buttons">
          <!-- Tombol Hapus (merah) -->
          <button class="delete-btn" @click="confirmDelete">Hapus</button>
          <!-- Tombol Batal (hijau) -->
          <button class="cancel-btn" @click="closeDeleteModal">Batal</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    todos: Array,
  },
  data() {
    return {
      showModal: false,
      editingTodo: null,
      editTitle: "",
      editPriority: 1,
      editDueDate: "",
      showDeleteModal: false,
      deletingTodo: null,
    };
  },
  methods: {
    // Edit Modal
    openEditModal(todo) {
      this.editingTodo = todo;
      this.editTitle = todo.title;
      this.editPriority = todo.priority;
      this.editDueDate = todo.due_date;
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
      this.editingTodo = null;
    },
    saveEdit() {
      if (!this.editTitle || !this.editDueDate) {
        alert("Judul dan deadline wajib diisi");
        return;
      }
      this.$emit("edit", {
        id: this.editingTodo.id,
        title: this.editTitle,
        priority: this.editPriority,
        due_date: this.editDueDate,
      });
      this.closeModal();
    },

    // Delete Modal
    openDeleteModal(todo) {
      this.deletingTodo = todo;
      this.showDeleteModal = true;
    },
    closeDeleteModal() {
      this.showDeleteModal = false;
      this.deletingTodo = null;
    },
    confirmDelete() {
      this.$emit("delete", this.deletingTodo.id);
      this.closeDeleteModal();
    },
  },
};
</script>
