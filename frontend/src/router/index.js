import { createWebHistory, createRouter } from "vue-router";
import Home from "../pages/Home.vue";
import About from "../pages/About.vue";
import Signup from "../pages/Signup.vue";
import Login from "../pages/Login.vue";
import NotFound from "../pages/NotFound.vue";
import Cart from "../pages/Cart.vue";
import Manager from "../pages/Manager.vue";
import Admin from "../pages/Admin.vue";
import ProductDetails from "../pages/ProductDetails.vue";
import Category from "../pages/Category.vue";
const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/cart",
    name: "Cart",
    component: Cart,
  },
  {
    path: "/manager",
    name: "Manager",
    component: Manager,
  },
  {
    path: "/admin",
    name: "Admin",
    component: Admin,
  },
  {
    path: "/productdetails/:id",
    name: "ProductDetails",
    component: ProductDetails,
  },
  {
    path:"/category/:id",
    name:"Category",
    component:Category,
  },
  {
    path: "/:catchAll(.*)",
    name: "NotFound",
    component: NotFound,
  },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;