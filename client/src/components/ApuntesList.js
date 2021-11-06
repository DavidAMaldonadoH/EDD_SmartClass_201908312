import Apunte from './Apunte';

function ApuntesList(props) {
	let apuntes = [];
	for (let i = 0; i < props.notes.length; i++) {
		const note = (
			<Apunte
				key={props.notes[i].ID}
				titulo={props.notes[i].Titulo}
				contenido={props.notes[i].Contenido}
			/>
		);
		apuntes.push(note);
	}
	return (
        <div>
            {apuntes}
        </div>
    );
}

export default ApuntesList;
