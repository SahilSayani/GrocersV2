<template>
    <div>
        <div class="manager-page">
    <!-- Manager Header -->
    <header>
      <h1>Manager Dashboard</h1>
    </header>
    <section class="send-summary">
      <h2>Export Summary</h2>
      <button @click="sendMonthlySummary">Send Summary</button>
    </section>

    <!-- Add New Category Section -->
    <section class="new-category">
      <h2>Create New Category</h2>
      <form @submit.prevent="createCategory">
        <input v-model="newCategoryName" type="text" placeholder="Category Name" required>
        <button type="submit">Create</button>
      </form>
    </section>

    <!-- Add New Product Section -->
    <section class="new-product">
      <h2>Add New Product</h2>
      <form @submit.prevent="addProduct">
        <div class="">productname</div>
        <input v-model="newProduct.name" type="text" placeholder="Product Name" required>
        <div class="">price</div>
        <input v-model="newProduct.price" type="number" placeholder="Price" required>
        <div class="">qty</div>
        <input v-model="newProduct.available_quantity" type="number" placeholder="Quantity" required>
        <div class="">category</div>
        <select v-model="newProduct.category_id">
          <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.name }}</option>
        </select>
        <div class="">image url</div>
        <input v-model="newProduct.image" type="text" placeholder="image url" required>
        <button type="submit">Add Product</button>
      </form>
    </section>

    <!-- Category and Product Listing -->
    <section class="category-listing">
      <div v-for="category in categories" :key="category.id">
        <h3>{{ category.name }}</h3>
        <ul>
          <li v-for="product in category.products" :key="product.id">
            {{ product.name }} - {{ product.price }} - {{ product.quantity }}
            <button @click="editProduct(product)">Edit</button>
            <button @click="deleteProduct(product.id)">Delete</button>
          </li>
        </ul>
      </div>
    </section>
  </div>
    </div>
</template>

<script>
export default {
  name: 'ManagerPage',
  data() {
    return {
      newCategoryName: '',
      newProduct: {
        name: '',
        price: 0,
        quantity: 0
      },
      categories: [] // This would be fetched from an API or static data
    }
  },
  mounted() {
    this.getCategories();
  },
  methods: {
    logout() {
      // Handle logout logic
    },
    getCategories(){
    fetch("http://127.0.0.1:5000/categories")
      .then((response) => response.json())
      .then((data) => {
        this.categories = data;
      })
      .catch((error) => {
        console.error("Error fetching categories:", error);
      });
    },
    createCategory() {
      // Logic to create a new category
      console.log (this.newCategoryName);
        fetch("http://127.0.0.1:5000/addcategory", {
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
        })

    },
    addProduct() {
        console.log(this.newProduct);
      // Logic to add a new product
      fetch("http://127.0.0.1:5000/product", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + localStorage.getItem("token"),
        },
        body: JSON.stringify(this.newProduct),
      })
        .then(() => {
          this.newProduct = {
            name: "",
            price: 0,
            quantity: 0,
          };
        })
        .catch((error) => {
          console.error("Error adding product:", error);
        });

    },
    sendMonthlySummary() {
    fetch("http://127.0.0.1:5000/summary", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + localStorage.getItem("token"),
      },
      body: JSON.stringify({
        email:localStorage.getItem("email"),
      }),
    })
    .then((response) => {
      if (response.ok) {
        console.log("Summary sent successfully");
      } else {
        console.error("Failed to send summary");
      }
    })
    .catch((error) => {
      console.error("Error sending summary:", error);
    });
  },

    editProduct(product) {
      // Logic to edit a product
    },
    deleteProduct(productId) {
      // Logic to delete a product
    }
  }
}
</script>

<style scoped>
.manager-page {
  /* Styles for the manager page */
}
</style>