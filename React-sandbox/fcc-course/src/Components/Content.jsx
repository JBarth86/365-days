export default function Content(props) {
    return (
        <main>
            <h1>I'm learning React because:</h1>
            <ol>
                {props.reasons.map((reason, i) => (
                    <li key={i}>{reason}</li>
                ))}
            </ol>
        </main>
    );
}
