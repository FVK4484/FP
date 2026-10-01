package fp.tipos.trenes;

import java.time.LocalTime;

public record Parada(String nombre, LocalTime horaLlegada, 
		LocalTime horaSalida) {
}
