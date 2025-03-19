import { BASE_BACKEND_URL } from "../../config";

const refreshAccessToken = async () => {
    try {
        const response = await fetch(`${BASE_BACKEND_URL}/auth/refresh`, {
            method: "GET",
            credentials: "include",
        });

        if (!response.ok) {
            throw new Error("Не удалось обновить токен");
        }

        const data = await response.json();
        document.cookie = `access_token=${data.access_token}; path=/; SameSite=Strict`;

        return data.access_token;
    } catch (error) {
        console.error("Ошибка при обновлении токена:", error);
        return null;
    }
};

export default refreshAccessToken;