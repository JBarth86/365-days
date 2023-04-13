import "./App.css";
import Header from "./Components/Header";
import Content from "./Components/Content";
import Footer from "./Components/Footer";
import React from "react";

export default function App() {
    return (
        <React.Fragment>
            <Header />
            <Content />
            <Footer />
        </React.Fragment>
    );
}
