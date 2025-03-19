import React from "react";

function OAuthButton({ provider, label, iconClass, onClick }) {
    return (
        <button className={provider.toLowerCase()} onClick={onClick}>
            <i className={iconClass}></i> {label}
        </button>
    );
}

export default OAuthButton;