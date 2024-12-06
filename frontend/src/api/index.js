import axios from "axios";

const defaultConfig = {
    headers: {
        'Content-type': 'application/json'
    }
}

const token = localStorage.getItem("token")
if (token) defaultConfig.headers['authorization'] = `Token ${token}`

export const DefaultAPIInstance = axios.create(defaultConfig);

