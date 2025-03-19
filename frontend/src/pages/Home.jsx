import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import refreshAccessToken from "../api/api";
import { BASE_BACKEND_URL } from "../../config";
import Cookies from "js-cookie";

function Home() {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchData = async () => {
            let accessToken = Cookies.get("access_token");

            if (!accessToken) {
                accessToken = await refreshAccessToken();
            }

            try {
                const response = await fetch(`${BASE_BACKEND_URL}/user/`, {
                    method: "GET",
                    headers: {
                        "Authorization": `Bearer ${accessToken}`,
                    },
                    credentials: "include",
                });

                if (response.status === 401) {
                    navigate("/auth");
                } else if (response.ok) {
                    const data = await response.json();
                    setUser(data);
                } else {
                    throw new Error(`Ошибка HTTP: ${response.status}`);
                }
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, [navigate]);

    const handleLogout = async () => {
        try {
            const accessToken = Cookies.get("access_token");
            const response = await fetch(`${BASE_BACKEND_URL}/auth/logout`, {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${accessToken}`,
                },
                credentials: "include",
            });

            if (!response.ok) {
                throw new Error(`Ошибка при выходе: ${response.status}`);
            }

            Cookies.remove("access_token");
            navigate("/auth");
        } catch (error) {
            console.error("Ошибка при выходе:", error);
        }
    };

    if (loading) {
        return <h1 className="loading">Загрузка...</h1>;
    }

    if (error) {
        return <h1 className="error">Ошибка: {error}</h1>;
    }

    return (
        <div className="container">
            <h1 className="title">Добро пожаловать!</h1>
            {user ? (
                <div className="user-info">
                    <p>Email: {user.email}</p>
                    <button className="logout-button" onClick={handleLogout}>Выход</button>
                </div>
            ) : (
                <p className="not-authenticated">Пользователь не авторизован.</p>
            )}
        </div>
    );
}

export default Home;
