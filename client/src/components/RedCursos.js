import { useState } from 'react';

import { Graphviz } from 'graphviz-react';

function RedCursos(props) {
	const [dotSrc, setDotSrc] = useState('graph { }');
	const [codigo, setCodigo] = useState('');

	const getDotSrc = async () => {
		const res = await fetch(`http://localhost:3000/redcursos/${codigo}`);
		const data = await res.json();
		setDotSrc(data.dotSrc);
	};

	const asignarCurso = async () => {
		const res = await fetch(`http://localhost:3000/asignarcurso/${props.account.carnet}/${codigo}`);
		const data = await res.json();
		alert(data.msg);
	};

	return (
		<div
			className="container d-flex align-items-start flex-column"
			style={{ marginTop: 0, paddingTop: 0 }}
		>
			<div className="keyContainer d-flex flex-row justify-content-center w-100">
				<label
					className="text-white text-center fw-bold bg-dark col-form-label"
					style={{ width: '35%', height: '50px' }}
				>
					Ingrese el Código del Curso a Analizar
				</label>
				<textarea
					className="form-control"
					style={{ resize: 'none', width: '35%', height: '50px' }}
					onChange={(e) => setCodigo(e.target.value)}
				></textarea>
				<button
					className="btn btn-success"
					style={{ width: '15%', height: '50px' }}
					onClick={getDotSrc}
				>
					Analizar
				</button>
				<button
					className="btn btn-info"
					style={{ width: '15%', height: '50px' }}
					onClick={asignarCurso}
				>
					Asignar
				</button>
			</div>
			<div className="mt-2">
				<Graphviz
					className="graphviz"
					dot={dotSrc}
					options={{
						height: 350,
						width: 1250,
					}}
				/>
			</div>
		</div>
	);
}

export default RedCursos;
