export default function Content(props) {
    return (
        <main>
            <h1 className="main-title">Fun facts about React</h1>
            <ul className="main-facts">
                {props.reasons.map((reason, i) => (
                    <li key={i}>{reason}</li>
                ))}
            </ul>
        </main>
    );
}
