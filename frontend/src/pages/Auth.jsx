import React from "react";
import OAuthButton from "../components/OAuthButton";
import { BASE_BACKEND_URL } from "../../config";

function Auth() {
    const providers = [
        {
            provider: "google",
            label: "Войти через Google",
            iconClass: "fab fa-google",
            url: `${BASE_BACKEND_URL}/auth/google/login`,
        },
        {
            provider: "yandex",
            label: "Войти через Yandex",
            iconClass: "fas fa-yandex",
            url: `${BASE_BACKEND_URL}/auth/yandex/login`,
        },
        {
            provider: "github",
            label: "Войти через GitHub",
            iconClass: "fab fa-github",
            url: `${BASE_BACKEND_URL}/auth/github/login`,
        },
    ];

    const handleOAuthLogin = (url) => {
        window.location.href = url;
    };

    return (
        <div className="auth-container">
            <h1>Авторизация через OAuth</h1>
            <div className="auth-buttons">
                {providers.map((provider, index) => (
                    <OAuthButton
                        key={index}
                        provider={provider.provider}
                        label={provider.label}
                        iconClass={provider.iconClass}
                        onClick={() => handleOAuthLogin(provider.url)}
                    />
                ))}
            </div>
        </div>
    );
}

export default Auth;