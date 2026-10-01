package fp.tipos;

import fp.utiles.Checkers;

public record Trayecto(String origen, String destino) {
	public Trayecto {
		Checkers.check("El origen del trayecto no puede ser el mismo que el destino."
				, !origen.equals(destino));
	}
}
