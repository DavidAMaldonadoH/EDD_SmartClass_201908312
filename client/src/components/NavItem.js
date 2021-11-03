import { NavLink } from 'react-router-dom';

function NavItem(props) {
	return (
		<li className="nav-item">
			<NavLink className="nav-link" to={`/${props.direccion}`} onClick={props.func}>
				{props.texto}
			</NavLink>
		</li>
	);
}

export default NavItem;
