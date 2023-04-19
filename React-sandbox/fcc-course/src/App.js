import "./App.css";
import Header from "./Components/Header";
import Content from "./Components/Content";
import Footer from "./Components/Footer";
import React from "react";

let reasons = [
    "Was first released in 2019",
    "Was originally created by Jordan Walke",
    "Has well over 100k stars on GitHub",
    "Is maintained by Facebook",
    "Powers thousands of enterprise apps, including mobile apps",
];

export default function App() {
    return (
        <React.Fragment>
            <Header />
            <div className="wrapper">
                <Content reasons={reasons} />
                <Footer />
            </div>
        </React.Fragment>
    );
}
