import "./App.css";
import Header from "./Components/Header";
import Content from "./Components/Content";
import Footer from "./Components/Footer";
import React from "react";

let reasons = [
    "It's a hireable skill",
    "It seems like the logical conclusion for web development",
    "Because I find it interesting",
];

export default function App() {
    return (
        <React.Fragment>
            <Header />
            <Content reasons={reasons} />
            <Footer />
        </React.Fragment>
    );
}
