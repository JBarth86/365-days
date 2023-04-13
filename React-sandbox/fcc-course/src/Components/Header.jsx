import hovalin from "../Images/hovalin.png";

export default function Header() {
    return (
        <header>
            <nav className="nav">
                <img src={hovalin} />
                <ul className="nav-items">
                    <li>Pricing</li>
                    <li>About</li>
                    <li>Contact</li>
                </ul>
            </nav>
        </header>
    );
}
