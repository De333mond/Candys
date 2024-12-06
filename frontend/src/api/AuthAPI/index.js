import {DefaultAPIInstance, LoginAPIInstance} from "@/api";

export const AuthAPI = {
    login(username, password) {
        const url = "http://localhost:8000/api/auth/token/login/"
        const data = {username, password}
        let response = LoginAPIInstance.post(url, data)
        console.log(response)
        return response
    },

    logout() {
        const url = "auth/token/logout/"
        return DefaultAPIInstance.post(url)
    }
}