import { useState } from 'react';
import { useHistory } from 'react-router';

import NavBar from './NavBar';
import userIcon from '../icons/user-solid.svg';
import Input from './Input';

function Register() {
	const history = useHistory();

	const [user, setUser] = useState({
		carnet: '',
		DPI: '',
		nombre: '',
		carrera: '',
		correo: '',
		password: '',
		creditos: 0,
		edad: 0,
	});

	const onChange = (name, value) => {
		switch (name) {
			case 'Carnet':
				setUser({ ...user, carnet: value });
				break;
			case 'DPI':
				setUser({ ...user, DPI: value });
				break;
			case 'Nombre':
				setUser({ ...user, nombre: value });
				break;
			case 'Carrera':
				setUser({ ...user, carrera: value });
				break;
			case 'Correo':
				setUser({ ...user, correo: value });
				break;
			case 'Password':
				setUser({ ...user, password: value });
				break;
			default:
				setUser({ ...user, edad: parseInt(value) });
				break;
		}
	};

	const addUser = async (user) => {
		const res = await fetch('http://localhost:3000/estudiante', {
			method: 'POST',
			headers: {
				'Content-type': 'application/json',
			},
			body: JSON.stringify(user),
		});

		const data = await res.json();
		console.log(data);
	};

	const onSubmit = (e) => {
		e.preventDefault();
		addUser(user);
		history.push('/login');
	};
	
	return (
		<>
			<NavBar />
			<div className="container d-flex justify-content-center">
				<div className="card text-center" style={{ minWidth: '50%' }}>
					<div className="row g-0">
						<div className="col-md-4 d-flex justify-content-center mt-4">
							<img
								src={userIcon}
								className="img-fluid"
								alt="user"
								style={{ height: '100px', width: '100px', margin: 'auto' }}
							/>
						</div>
						<div className="col-md-8">
							<div className="card-body">
								<h5 className="card-title">Registro</h5>
								<form onSubmit={onSubmit}>
									<Input texto="Carnet" tipo="text" onChange={onChange} />
									<Input texto="DPI" tipo="text" onChange={onChange} />
									<Input texto="Nombre" tipo="text" onChange={onChange} />
									<Input texto="Carrera" tipo="text" onChange={onChange} />
									<Input texto="Correo" tipo="email" onChange={onChange} />
									<Input texto="Password" tipo="password" onChange={onChange} />
									<Input texto="Edad" tipo="text" onChange={onChange} />
									<button className="w-100 btn btn-primary" type="submit">
										Sign up
									</button>
								</form>
							</div>
						</div>
					</div>
				</div>
			</div>
		</>
	);
}

export default Register;
