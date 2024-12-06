// Импорт библиотеки Axios для выполнения HTTP-запросов
import axios from "axios";

// Экспорт модуля ProductsModule
export const ProductsModule = {
  namespaced: true, // Пространство имен для модуля

  state() {
    return {
      products: [] // Начальное состояние: пустой массив продуктов
    };
  },

  mutations: {
    // Мутация для установки продуктов в состояние
    setProductsToState(state, payload) {
      state.products = payload;
    }
  },

  getters: {
    // Геттер для получения продуктов со значением "sale" в поле adv_state
    getOnSale(state) {
      return state.products.filter((el) => el.adv_state === "sale");
    }
  },

  actions: {
    // Действие для добавления продукта в состояние
    addItem({ commit }, payload) {
      commit("addProductToState", payload); // Вызов соответствующей мутации
    },

    // Действие для получения продуктов из API
    fetchProducts({ commit }) {
      let url = "http://127.0.0.1:8000/api/products/";

      axios
        .get(url) // Выполнение GET-запроса с использованием Axios
        .then((response) => {
          commit("setProductsToState", response.data); // Вызов мутации для установки продуктов в состояние
        })
        .catch((error) => {
          console.log(error); // Обработка ошибок
        });
    }
  }
};
