function Header() {
    return (
        <header>
            <nav>
                <img
                    src="../../April/4-8-2023-day-17/hovalin.png"
                    width="100"
                />
            </nav>
        </header>
    );
}

function Content() {
    return (
        <main>
            <h1>I'm learning React because:</h1>
            <ol>
                <li>It's a hireable skill</li>
                <li>
                    It seems like the logical conclusion for web development
                </li>
                <li>Because I find it interesting</li>
            </ol>
        </main>
    );
}

function Footer() {
    return (
        <footer>
            <small>
                <p>&copy; 2023 Shocking Development</p>
            </small>
        </footer>
    );
}

function Page() {
    return (
        <div>
            <Header />
            <Content />
            <Footer />
        </div>
    );
}

ReactDOM.render(<Page />, document.getElementById("root"));
