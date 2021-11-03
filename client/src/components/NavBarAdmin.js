import { NavLink } from 'react-router-dom';
import NavItem from './NavItem';

function NavBarAdmin(props) {
	return (
		<nav className="navbar navbar-expand-sm navbar-dark bg-dark">
			<div className="container-fluid">
				<NavLink className="navbar-brand" to="/">
					Smart Class
				</NavLink>
				<button
					className="navbar-toggler"
					type="button"
					data-bs-toggle="collapse"
					data-bs-target="#navbarNav"
					aria-controls="navbarNav"
					aria-expanded="false"
					aria-label="Toggle navigation"
				>
					<span className="navbar-toggler-icon" />
				</button>
				<div className="collapse navbar-collapse" id="navbarNav">
					<ul className="navbar-nav ms-auto">
						<NavItem texto="Log Out" direccion="login" func={props.onLogOut} />
					</ul>
				</div>
			</div>
		</nav>
	);
}

export default NavBarAdmin;
