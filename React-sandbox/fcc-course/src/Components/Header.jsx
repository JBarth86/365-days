import logo from "../logo.svg";

export default function Header() {
    return (
        <header>
            <nav className="nav">
                <img className="logo-img" src={logo} />
                <h3 className="logo-text">ReactFacts</h3>
                <h4 className="page-name">React Course - Project 1</h4>
            </nav>
        </header>
    );
}
