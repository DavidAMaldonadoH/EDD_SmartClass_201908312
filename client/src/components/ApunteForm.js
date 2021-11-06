import { useState } from 'react';

function ApunteForm(props) {
	const [note, setNote] = useState({ carnet: props.account.carnet, titulo: '', contenido: '' });
	
	const saveNote = async () => {
		const res = await fetch(`http://localhost:3000/apuntes_usuario/${props.account.carnet}`, {
			method: 'POST',
			headers: {
				'Content-type': 'application/json',
			},
			body: JSON.stringify(note),
		});
		const data = await res.json();
		alert(data.msg);
	};

	const onChange = (name, value) => {
		if (name === 'titulo') {
			setNote({ ...note, titulo: value });
		} else {
			setNote({ ...note, contenido: value });
		}
	};

	return (
		<div className="m-4">
			<div className="mb-3 row">
				<label htmlFor="carnetApunte" className="col-sm-2 col-form-label">
					Carnet
				</label>
				<div className="col-sm-10">
					<input
						type="text"
						className="form-control"
						id="carnetApunte"
						placeholder={props.account.carnet}
						readOnly
					/>
				</div>
			</div>
			<div className="mb-3 row">
				<label htmlFor="tituloApunte" className="col-sm-2 col-form-label">
					Titulo
				</label>
				<div className="col-sm-10">
					<input
						type="text"
						className="form-control"
						id="tituloApunte"
						placeholder="Apunte 1"
						name="titulo"
						onChange={(e) => onChange(e.target.name, e.target.value)}
					/>
				</div>
			</div>
			<div>
				<label htmlFor="exampleFormControlTextarea1" className="form-label">
					Contenido
				</label>
				<textarea
					className="form-control"
					id="exampleFormControlTextarea1"
					name="contenido"
					rows={3}
					defaultValue={''}
					onChange={(e) => onChange(e.target.name, e.target.value)}
				/>
			</div>
			<div className="text-end">
				<button className="btn btn-primary mt-4" onClick={saveNote}>
					Guardar
				</button>
			</div>
		</div>
	);
}

export default ApunteForm;
