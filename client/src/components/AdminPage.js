import { useState } from 'react';

import Key from './Key';
import NavBarAdmin from './NavBarAdmin';
import Reportes from './Reportes';

function AdminPage(props) {
	const [key, setKey] = useState('');
	const [value, setValue] = useState('');

	const fetchKey = async () => {
		const res = await fetch('http://localhost:3000/adminKey');
		const data = await res.json();
		setKey(data.adminKey);
		localStorage.setItem('adminKey', data.adminKey);
	};

	const onChange = (e) => {
		const reader = new FileReader();
		reader.addEventListener('load', function (ev) {
			setValue(ev.target.result);
		});
		reader.readAsText(e.target.files[0]);
	};

	const addEstudiantes = async () => {
		const res = await fetch('http://localhost:3000/users', {
			method: 'POST',
			headers: {
				'Content-type': 'application/json',
			},
			body: value,
		});
		const data = await res.json();
		alert(data.msg);
	};

	const addCursos = async () => {
		const res = await fetch('http://localhost:3000/cursosPensum', {
			method: 'POST',
			headers: {
				'Content-type': 'application/json',
			},
			body: value,
		});
		const data = await res.json();
		alert(data.msg);
	};

	const addCursosEst = async () => {
		const res = await fetch('http://localhost:3000/cursosEstudiante', {
			method: 'POST',
			headers: {
				'Content-type': 'application/json',
			},
			body: value,
		})
		const data = await res.json();
		alert(data.msg)
	}

	const addApuntes = async () => {
		const res = await fetch('http://localhost:3000/apuntes', {
			method: 'POST',
			headers: {
				'Content-type': 'application/json',
			},
			body: value,
		});
		const data = await res.json();
		alert(data.msg)
	};

	return (
		<>
			<NavBarAdmin onLogOut={props.onLogOut} />
			<div className="container d-flex align-items-start flex-column">
				<Key texto={key} getKey={fetchKey} />
				<div className="mt-3 d-flex w-100">
					<input
						className="form-control"
						type="file"
						id="formFile"
						onChange={onChange}
						style={{ width: '35%' }}
					/>
					<label
						className="text-white text-center bg-dark col-sm-2 col-form-label"
						style={{ width: '15%' }}
					>
						Carga Masiva
					</label>
					<div className="btn-group w-50" role="group">
						<button type="button" className="btn btn-outline-primary" onClick={addEstudiantes}>
							Estudiantes
						</button>
						<button type="button" className="btn btn-outline-primary" onClick={addCursos}>
							Cursos Pensum
						</button>
						<button type="button" className="btn btn-outline-primary" onClick={addCursosEst}>
							Cursos Estudiante
						</button>
						<button type="button" className="btn btn-outline-primary" onClick={addApuntes}>
							Apuntes
						</button>
					</div>
				</div>
				<textarea className="w-100 mt-3 form-control" readOnly rows={15} value={value}></textarea>
				<Reportes />
			</div>
		</>
	);
}

export default AdminPage;
