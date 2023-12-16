<script setup>
import Nav from "../components/Nav.vue";
import CategoryItem from "../components/CategoryItem.vue";
import ProductCard from "../components/ProductCard.vue";
import Searchbar from "../components/Searchbar.vue";
import { RouterLink } from "vue-router";
</script>

<template>
  <div>
    <div class="headcontainer">
      <img src="../assets/hero img.png" class="heroimg" />
      <div class="intro">
        <div class="typography">
          Get fresh groceries delivered to your doorstep
        </div>
        <div class="typography2">
          The best delivery app in town for delivering you daily fresh groceries
        </div>
        <button class="shopnow">Shop Now</button>
      </div>
    </div>
    <div class="flex categories">
      <div class="typography">Categories😋</div>
    </div>
    <div class="categories">
      <ul>
        <li v-for="category in categories" :key="category">
          <div class="card">
            <RouterLink class="cardData" :to="`/category/${category.id}`"
              >{{ category.name }}
            </RouterLink>
          </div>
        </li>
      </ul>
    </div>

    <div class="categories">
      <div class="typography">Best Selling 🔥</div>
      <a href="#products" class="typography2 greentext">See All</a>
    </div>
    <Searchbar @search="filterProducts" />

    <ul>
      <li v-for="product in filteredProducts" :key="product.id">
        <!-- Display your product details here -->
        <ProductCard
          :id="product.id"
          :name="product.name"
          :price="product.price"
          :available-quantity="product.availableQuantity"
          :category-id="product.categoryId"
          :image="product.image"
        />
      </li>
    </ul>

    <div class="flex categories">
      <div v-for="product in products" :key="product.id">
        <ProductCard
          :id="product.id"
          :name="product.name"
          :price="product.price"
          :available-quantity="product.availableQuantity"
          :category-id="product.categoryId"
          :image="product.image"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    categories: [],
    products: [],
    filteredProducts: [], // Filtered products based on the search query
  }),
  mounted() {
    // Fetch categories from the Flask API
    fetch("http://127.0.0.1:5000/categories")
      .then((response) => response.json())
      .then((data) => {
        this.categories = data;
      })
      .catch((error) => {
        console.error("Error fetching categories:", error);
      });
    fetch("http://127.0.0.1:5000/products")
      .then((response) => response.json())
      .then((data) => {
        this.products = data;
      })
      .catch((error) => {
        console.error("Error fetching products:", error);
      });
  },
  methods: {
    filterProducts(query) {
      // Implement your search logic here, e.g., filter products based on query
      this.filteredProducts = this.products.filter((product) => {
        // Example: Filter by product name
        return product.name.toLowerCase().includes(query.toLowerCase());
      });
    },
  },
  components: {
    Nav,
    CategoryItem,
    ProductCard,
    Searchbar,
  },
};
</script>

<style>
.intro {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  margin-left: 10%;
}
.headcontainer {
  background: url(../assets/leaf1.png), url(../assets/leaf2.png),
    url(../assets/leaf1.png), url(../assets/leaf2.png);
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: 80% 15%, 90% 35%, 45% 35%, 55% 20%;

  margin-left: 3%;
  margin-top: 3%;
  display: flex;
  align-items: center;
  gap: 32px;
}
.shopnow {
  margin-top: 3%;
  display: flex;
  width: 33%;
  padding: 16px 8px;
  justify-content: center;
  align-items: center;
  border-radius: 100px;
  border: none;
  cursor: pointer;
  background: #23aa49;
}
.heroimg {
  width: 35%;
}

.categories {
  margin: 2%;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 5rem;
  flex-wrap: wrap;
}
.categories > a {
  text-decoration: none;
  flex-direction: column;
}

.categorylist {
  flex-direction: row;
}
ul {
  list-style-type: none;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}
.card {
  width: 7rem;
  height: 5rem;
  margin: auto;
  flex-shrink: 0;
  background: #1a3848;
  border-radius: 16px;
  margin: 1rem;
}

.cardData {
  text-decoration: none;
  color: white;
  position: absolute;
}
.cardData:hover {
  color: #23aa49;
}
</style>
