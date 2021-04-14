import axios from "axios";

import baseURL from "@/util/api";

const http = axios.create({
    baseURL: baseURL,
    timeout: 500000,
    contentType: "application/json"
});

http.axios = axios;

http.interceptors.request.use();

http.interceptors.response.use();

export default http;
