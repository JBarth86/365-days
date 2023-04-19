export default function Content(props) {
    return (
        <main>
            <h1>Fun facts about react</h1>
            <ul>
                {props.reasons.map((reason, i) => (
                    <li key={i}>{reason}</li>
                ))}
            </ul>
        </main>
    );
}
