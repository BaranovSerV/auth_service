import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { BASE_BACKEND_URL } from "../../config";

function AuthGithub() {
    const navigate = useNavigate();
    const [isCodeProcessed, setIsCodeProcessed] = useState(false);

    useEffect(() => {
        const params = new URLSearchParams(window.location.search);
        const code = params.get("code");

        if (isCodeProcessed || !code) {
            navigate("/");
            return;
        }

        window.history.replaceState({}, document.title, "/auth/github");

        fetch(`${BASE_BACKEND_URL}/auth/github/callback?code=${code}`, {
            method: "GET",
            credentials: "include",
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`Ошибка HTTP: ${response.status}`);
                }
                return response.json();
            })
            .then((data) => {
                console.log("Токены успешно получены:", data);

                setIsCodeProcessed(true);
                navigate("/");
            })
            .catch((error) => {
                console.error("Ошибка при обмене кода на токены:", error);
                alert("Произошла ошибка при авторизации. Попробуйте позже.");

                setIsCodeProcessed(true);
            });
    }, [navigate, isCodeProcessed]);

    return <h1>Обработка авторизации...</h1>;
}

export default AuthGithub;