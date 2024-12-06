import {DefaultAPIInstance} from "@/api";
import axios from "axios";

export const AuthModule = {
    namespaced: true,
    state() {
        return {
            credentials: {
                token: localStorage.getItem("token") || null,
            },
            hasError: false,
            currentUser: null,
        }
    },

    mutations: {
        setToken(state, token) {
            state.credentials.token = token;
            localStorage.setItem("token", token);
        },

        deleteToken(state) {
            state.credentials.token = null;
            localStorage.removeItem("token");
        },

        setCurrentUser(state, payload) {
            state.currentUser = payload;
        },

        deleteCurrentUser(state) {
            state.currentUser = null;
        },
    },

    actions: {
        onLogin({commit, dispatch}, {username, password}) {
            axios.post("http://localhost:8000/api/auth/token/login/", {
              username: username,
              password: password,
            }).then((response) => {
                commit("setToken", response.data.auth_token)
                DefaultAPIInstance.defaults.headers["authorization"] = `Token ${response.data.auth_token}`
                this.state.hasError = false;
                this.state.isAuth = true;
            }).catch((e) => {
                console.log("Error", e)
                this.state.hasError = true;
            })
        },

        onLogout({commit}) {
            DefaultAPIInstance.post("http://localhost:8000/api/auth/token/logout/")
            commit("deleteToken")
            commit("deleteCurrentUser")
            delete DefaultAPIInstance.defaults.headers["authorization"]
            this.state.isAuth = false
        },

        onSignUp({commit, dispatch}, {username, password, re_password}) {
            console.log({username, password, re_password})
            axios
                .post('http://localhost:8000/api/auth/users/', {username, password, re_password})
                .then(resp => dispatch('onLogin', {username, password}))
                .catch(e => console.log(e))
        },

        fetchUserInformation({state, commit}) {
            if (state.credentials.token === '')
                return;

            axios.get("http://localhost:8000/api/auth/users/me/", {
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": "Token " + state.credentials.token,
                    }
                })
                .then(response => {
                    commit("setCurrentUser", response.data);
                })
                .then(() => {
                    if (state.currentUser.customer !== null)
                        DefaultAPIInstance
                            .get('http://localhost:8000/api/customers/' + state.currentUser.customer + "/")
                            .then(resp => commit('setAdditionalUserInfo', resp.data))
                            .catch(e => console.log(e))
                })
                .catch(e => {console.log(e)})
        },

        updateUserInformation({commit, state}, {customer, user}) {
            let apiInstance = axios.create({
                headers: {
                    "Authorization": "Token " + state.credentials.token,
                    "Content-Type": "application/json"
                }})

            if (!state.currentUser.customer) {
                apiInstance
                    .post('http://localhost:8000/api/customers/', customer)
                    .then(resp => {
                        commit('setCurrentUserInformation', resp.data.id)
                        commit('setAdditionalUserInfo', resp.data)
                    })
                    .catch(e => console.log(e))
            }
            else {
                apiInstance
                    .put('http://localhost:8000/api/customers/' + state.currentUser.customer + "/", customer)
                    .then(resp => {
                        commit('setCurrentUserInformation', resp.data.id)
                        commit('setAdditionalUserInfo', resp.data)
                    })
                    .catch(e => console.log(e))
            }
            apiInstance.put('http://localhost:8000/api/auth/users/me/', {...user, customer: state.currentUser.customer})
                .then(resp => commit('setCurrentUser', resp.data))
                .catch(e => console.log(e))
        },
    },
}