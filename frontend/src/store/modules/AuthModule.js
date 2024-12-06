// Импорт необходимых модулей и библиотек
import { DefaultAPIInstance } from "@/api";
import axios from "axios";

// Экспорт модуля AuthModule
export const AuthModule = {
  namespaced: true, // Пространство имен для модуля

  state() {
    return {
      credentials: {
        token: localStorage.getItem("token") || null, // Поле для хранения токена аутентификации
      },
      hasError: false, // Флаг для отслеживания наличия ошибки
      currentUser: null, // Текущий пользователь
      userInfo: null, // Дополнительная информация о пользователе
    };
  },

  mutations: {
    // Мутация для установки токена в состояние
    setToken(state, token) {
      state.credentials.token = token;
      localStorage.setItem("token", token); // Сохранение токена в localStorage
    },

    // Мутация для удаления токена из состояния
    deleteToken(state) {
      state.credentials.token = null;
      localStorage.removeItem("token"); // Удаление токена из localStorage
    },

    // Мутация для установки текущего пользователя
    setCurrentUser(state, payload) {
      state.currentUser = payload;
    },

    // Мутация для удаления текущего пользователя
    deleteCurrentUser(state) {
      state.currentUser = null;
    },

    // Мутация для установки информации о текущем пользователе
    setCurrentUserInformation(state, payload) {
      state.currentUser.customer = payload;
    },

    // Мутация для установки дополнительной информации о пользователе
    setAdditionalUserInfo(state, payload) {
      state.userInfo = payload;
    },
  },

  actions: {
    // Действие для входа пользователя в систему
    onLogin({ commit, dispatch }, { username, password }) {
      axios
        .post("http://localhost:8000/api/auth/token/login/", {
          username: username,
          password: password,
        })
        .then((response) => {
          commit("setToken", response.data.auth_token); // Установка полученного токена в состояние
          DefaultAPIInstance.defaults.headers[
            "authorization"
          ] = `Token ${response.data.auth_token}`; // Установка заголовка авторизации для дальнейших запросов
          this.state.hasError = false; // Сброс флага ошибки
          this.state.isAuth = true; // Установка флага аутентификации
        })
        .then(() => {
          dispatch("fetchUserInformation"); // Вызов действия для получения информации о пользователе
        })
        .catch((e) => {
          console.log("Error", e);
          this.state.hasError = true; // Установка флага ошибки
        });
    },

    // Действие для выхода пользователя из системы
    onLogout({ commit }) {
      DefaultAPIInstance.post("http://localhost:8000/api/auth/token/logout/");
      commit("deleteToken"); // Вызов мутации для удаления токена из состояния
      commit("deleteCurrentUser"); // Вызов мутации для удаления текущего пользователя
      delete DefaultAPIInstance.defaults.headers["authorization"]; // Удаление заголовка авторизации
      this.state.isAuth = false; // Сброс флага аутентификации
    },

    // Действие для регистрации нового пользователя
    onSignUp({ commit, dispatch }, { username, password, re_password }) {
      console.log({ username, password, re_password });
      axios
        .post("http://localhost:8000/api/auth/users/", {
          username,
          password,
          re_password,
        })
        .then((resp) =>
          dispatch("onLogin", { username, password }) // Вызов действия для входа пользователя после успешной регистрации
        )
        .catch((e) => console.log(e));
    },

    // Действие для получения информации о пользователе
    fetchUserInformation({ state, commit }) {
      if (state.credentials.token === "") return;

      axios
        .get("http://localhost:8000/api/auth/users/me/", {
          headers: {
            "Content-Type": "application/json",
            Authorization: "Token " + state.credentials.token,
          },
        })
        .then((response) => {
          commit("setCurrentUser", response.data); // Установка текущего пользователя в состояние
        })
        .then(() => {
          if (state.currentUser.customer !== null) {
            DefaultAPIInstance.get(
              "http://localhost:8000/api/customers/" +
                state.currentUser.customer +
                "/"
            )
              .then((resp) => commit("setAdditionalUserInfo", resp.data)) // Установка дополнительной информации о пользователе в состояние
              .catch((e) => console.log(e));
          }
        })
        .catch((e) => {
          console.log(e);
        });
    },

    // Действие для обновления информации о пользователе
    updateUserInformation({ commit, state }, { customer, user }) {
      let apiInstance = axios.create({
        headers: {
          Authorization: "Token " + state.credentials.token,
          "Content-Type": "application/json",
        },
      });

      if (!state.currentUser.customer) {
        apiInstance
          .post("http://localhost:8000/api/customers/", customer)
          .then((resp) => {
            commit("setCurrentUserInformation", resp.data.id); // Установка информации о текущем пользователе в состояние
            commit("setAdditionalUserInfo", resp.data); // Установка дополнительной информации о пользователе в состояние
          })
          .catch((e) => console.log(e));
      } else {
        apiInstance
          .put(
            "http://localhost:8000/api/customers/" +
              state.currentUser.customer +
              "/",
            customer
          )
          .then((resp) => {
            commit("setCurrentUserInformation", resp.data.id); // Установка информации о текущем пользователе в состояние
            commit("setAdditionalUserInfo", resp.data); // Установка дополнительной информации о пользователе в состояние
          })
          .catch((e) => console.log(e));
      }
      apiInstance
        .put("http://localhost:8000/api/auth/users/me/", {
          ...user,
          customer: state.currentUser.customer,
        })
        .then((resp) => commit("setCurrentUser", resp.data)) // Установка текущего пользователя в состояние
        .catch((e) => console.log(e));
    },
  },
};
