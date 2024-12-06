import {createWebHistory, createRouter} from "vue-router/dist/vue-router";
import MainPage from "@/pages/MainPage";
import ProductsPage from "@/pages/ProductsPage";
import AboutUsPage from "@/pages/AboutUsPage";
import BaseLayout from "@/pages/Layouts/BaseLayout";
import CustomOrderPage from "@/pages/CustomOrderPage";
import LoginPage from "@/pages/Login";
import UserPage from "@/pages/UserPage";
import MakeOrderPage from "@/pages/MakeOrderPage";
import store from "@/store/index.js"
import CourtPage from "@/pages/CourtPage";
import ProductPage from "@/pages/ItemPage";
import v404Page from "@/pages/v-404-page";
import test from "@/pages/test";
import SuccessfulPage from "@/pages/SuccessfulPage";
import registerPage from "@/pages/register-page";

const routes = [

    {
        path: "/",
        name: "base",
        component: BaseLayout,
        children: [
            {
                path: "/",
                name: "home",
                component: MainPage,
            },
            {
                path: "/products",
                name: "products",
                component: ProductsPage,
            },
            {
                path: "/about-us",
                name: "aboutUs",
                component: AboutUsPage,
            },
            {
                path: "/custom",
                name: "custom",
                component: CustomOrderPage,
            },
            {
                path: "/login",
                name: "login",
                component: LoginPage,
            },
            {
                path: "/me",
                name: "UserPage",
                component: UserPage,
                meta: {requireAuth: true},
            },
            {
                path: "/order",
                name: "MakeOrder",
                component: MakeOrderPage,
                meta: {requireAuth: true},
            },
            {
                path: "/court",
                name: "CourtPage",
                component: CourtPage,
            },
            {
                path: "/successful",
                name: "successful",
                component: SuccessfulPage,
            },
            {
                path: "/register",
                name: "sign-up",
                component: registerPage
            },
            {
                path: "/products/:filter?",
                name: "products",
                component: ProductsPage,
            },
            {
                path: "/item/:id",
                name: "Item",
                component: ProductPage,
            },

        ],
    },
    {
        path: '/:pathMatch(.*)*',
        name: "404",
        component: v404Page,
    }
];


let router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    if (store.state.AuthModule.credentials.token === null && to.meta.requireAuth)
        next('login')
    else
        next()
})

export default router;


