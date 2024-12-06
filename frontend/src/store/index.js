import {AuthModule} from "@/store/modules/AuthModule";
import {CourtModule} from "@/store/modules/CourtModule"
import Vuex from "vuex"
import {ProductsModule} from "@/store/modules/ProductsModule";

let store = new Vuex.Store({
    modules: {
        AuthModule, CourtModule, ProductsModule
    }
})

export default store;