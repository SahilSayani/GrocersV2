<template>
  <header>
    <h1>Admin Dashboard</h1>
    {{ categories }}
  </header>
  <div class="admin-page">
    <button @click="test">test</button>
    <!-- Pending Category Approvals -->
    <section class="pending-approvals">
      <h2>Pending Category Approvals</h2>
      <div class="thcontainer">
        <thead>
          <th width="300">Pending Categories</th>

          <th width="150">Action</th>
        </thead>
      </div>
      <table>
        <tbody>
          <tr v-for="category in categories" :key="category.id">
            <td width="300">{{ category.name }}</td>
            <td width="150">
              <button class="decisionbtn" @click="acceptCategory(category.id)">
                Accept
              </button>
              <button
                class="rejectdecisionbtn"
                @click="rejectCategory(category.id)"
              >
                Reject
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- Create New Category -->
    <section class="create-category">
      <h2>Create New Category</h2>
      <form @submit.prevent="createCategory">
        <input
          type="text"
          v-model="newCategoryName"
          placeholder="Category Name"
        />
        <button type="submit">Create</button>
      </form>
    </section>

    <!-- Existing Categories -->
    <section class="existing-categories">
      <h2>Existing Categories</h2>
      <div class="thcontainer">
        <thead>
          <th width="300">Current Categories</th>

          <th width="150">Action</th>
        </thead>
      </div>
      <table>
        <tbody>
          <tr v-for="category in activecategories" :key="category.id">
            <td width="300">{{ category.name }}</td>
            <td width="150">
              <button
                class="editdecisionbtn"
                @click="editCategory(category.id)"
              >
                Edit
              </button>
              <button
                class="rejectdecisionbtn"
                @click="deleteCategory(category.id)"
              >
                Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </section>
  </div>
</template>

<script>
import { API_URL } from "../constants";

export default {
  name: "AdminPage",
  data() {
    return {
      categories: [],
      activecategories: [],
      newCategoryName: "",
    };
  },
  computed: {},
  mounted() {
    this.getCategories();
    this.getActiveCategories();
  },
  methods: {
    getCategories() {
      fetch("http://127.0.0.1:5000/pendingcategories", {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("token"),
        },
      })
        .then((response) => response.json())
        .then((data) => {
          this.categories = data;
        })
        .catch((error) => {
          console.error("Error fetching categories:", error);
        });
    },
    getActiveCategories() {
      fetch("http://127.0.0.1:5000/categories")
        .then((response) => response.json())
        .then((data) => {
          this.activecategories = data;
        })
        .catch((error) => {
          console.error("Error fetching categories:", error);
        });
    },
    acceptCategory(id) {
      // API call to accept the category
      // Update categories list
      fetch("http://127.0.0.1:5000/category", {
        method: "PATCH",
        body: JSON.stringify({
          id,
        }),
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + localStorage.getItem("token"),
        },
      })
        .then(() => {
          this.getCategories();
          this.getActiveCategories();
        })
        .catch((error) => {
          console.error("Error fetching categories:", error);
        });
    },
    rejectCategory(id) {
      fetch(API_URL + "/category/" + id, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + localStorage.getItem("token"),
        },
      }).then(() => this.getCategories());
    },
    createCategory() {
      console.log (this.newCategoryName);
        fetch("http://127.0.0.1:5000/adminaddcategory", {
        method: "POST",
        headers:{
            "Content-Type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem("token"),
        },
        body: JSON.stringify({
            name: this.newCategoryName,
        }),
        })
        .then(() => {
            this.newCategoryName = "";
            this.getActiveCategories();
        })
        

    },
    deleteCategory(id) {
      fetch(API_URL + "/category/" + id, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + localStorage.getItem("token"),
        },
      }).then(() => this.getActiveCategories());
    },
    editCategory(id) {
      const newName = prompt("Enter new name");

      fetch(API_URL + "/category/" + id, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + localStorage.getItem("token"),
        },
        body: JSON.stringify({
          name: newName,
        }),
      }).then(() => this.getActiveCategories());
    },
  },
};
</script>

<style scoped>
/* Add your custom styles here if needed */
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

th,
td {
  border: 1px solid #23aa49;
  padding: 8px;
  text-align: left;
}

thead {
  display: table-header-group;
}

tbody {
  display: table-row-group;
}
.decisionbtn {
  background-color: #23aa49;
  color: white;
  padding: 5px 10px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
  margin-right: 5px;
}
.editdecisionbtn {
  background-color: #e2c130;
  color: rgb(0, 0, 0);
  padding: 5px 15px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
  margin-right: 5px;
}
.rejectdecisionbtn {
  background-color: #e74c3c;
  color: white;
  padding: 5px 10px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
  margin-right: 5px;
}
.rejectdecisionbtn:hover {
  background-color: #ac2a1c;
}
.editdecisionbtn:hover {
  background-color: #b8ab20;
}
.decisionbtn:hover {
  background-color: rgb(25, 141, 58);
}
.tablehead {
  background-color: #23aa49;
  color: white;
}
.thcontainer {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
